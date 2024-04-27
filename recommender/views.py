from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv
from recommender.models import InfluensysInfluencers
from recommender.serializers import InfluencerQuickSerializer

load_dotenv()


def connect_db():
    conn = psycopg2.connect(
        database=os.environ.get('POSTGRES_DATABASE'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host=os.environ.get('POSTGRES_HOST'),
        port="5432"
    )
    return conn


def get_data_marketers(buisness_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, industry FROM influensys_influencers;")
    industries = cur.fetchall()
    df = pd.DataFrame(industries, columns=['id', 'industry_type'])
    cur.execute(
        """SELECT influencer_id, target_age, target_gender, target_income_level, selected_interests, communication_channel FROM influensys_targetinfo;""")
    demographics = cur.fetchall()
    demographics = pd.DataFrame(demographics, columns=['id', 'target_audience_age_range', 'target_audience_gender',
                                                       'target_audience_income_range',
                                                       'interests', 'communication_channel'])
    data = pd.merge(df, demographics, how='outer', on=['id'])

    cur.execute("SELECT id, industry FROM buisness_businesses WHERE id = {0}".format(buisness_id))
    industries = cur.fetchall()
    df = pd.DataFrame(industries, columns=['id', 'industry_type'])
    cur.execute(
        """SELECT business_id, age, gender, income_level, selected_interests, communication_channel FROM buisness_businessgoals;""")
    demographics = cur.fetchall()
    demographics = pd.DataFrame(demographics, columns=['id', 'target_audience_age_range', 'target_audience_gender',
                                                       'target_audience_income_range',
                                                       'interests', 'communication_channel'])
    business = pd.merge(df, demographics, how='outer', on=['id'])
    # print(business)
    return data, business


def get_data_campaigns(campaign_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, industry FROM influensys_influencers;")
    industries = cur.fetchall()
    df = pd.DataFrame(industries, columns=['id', 'industry_type'])
    cur.execute(
        """SELECT influencer_id, target_age, target_gender, target_income_level, selected_interests, communication_channel FROM influensys_targetinfo;""")
    demographics = cur.fetchall()
    demographics = pd.DataFrame(demographics, columns=['id', 'target_audience_age_range', 'target_audience_gender',
                                                       'target_audience_income_range',
                                                       'interests', 'communication_channel'])
    data = pd.merge(df, demographics, how='outer', on=['id'])

    cur.execute(
        """SELECT id, target_age, target_gender, target_income_level, interests, communication_channel FROM buisness_campaigns WHERE campaign_id ={0}""".format(
            campaign_id)
    )
    campaign = cur.fetchall()
    campaign = pd.DataFrame(demographics, columns=['id', 'target_audience_age_range', 'target_audience_gender',
                                                   'target_audience_income_range',
                                                   'interests', 'communication_channel'])
    campaign_data = pd.merge(df, campaign, how='outer', on=['id'])

    return data, campaign_data


def convert_to_str(row):
    # print(row)
    return ', '.join(list(row))


def preprocess_data(data):
    df = data.fillna('')
    df['industry_type'] = df["industry_type"].apply(convert_to_str)
    df['interests'] = df["interests"].apply(convert_to_str)
    df['target_audience_age_range'] = df["target_audience_age_range"].apply(convert_to_str)
    df['target_audience_income_range'] = df["target_audience_income_range"].apply(
        convert_to_str)
    df['target_audience_gender'] = df["target_audience_gender"].apply(convert_to_str)
    df['communication_channel'] = df["communication_channel"].apply(convert_to_str)
    return df


def get_recommendations(influencer_df, nd_sample):
    print(type(nd_sample.tolist()))
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(
        influencer_df['industry_type'] + " " +
        influencer_df['interests'] + " " +
        influencer_df['target_audience_age_range'] + " " +
        influencer_df['target_audience_income_range'] + " " +
        influencer_df['target_audience_gender'] + " " +
        influencer_df['communication_channel'])
    target_audience_vector = tfidf_vectorizer.transform([' '.join(map(str, nd_sample.tolist()))])
    similarity_scores = cosine_similarity(target_audience_vector, tfidf_matrix)
    similarity_scores_for_marketer = similarity_scores[0]
    top_influencer_indices = similarity_scores_for_marketer.argsort()[:-5][::-1]
    top_influencers = influencer_df.iloc[top_influencer_indices]

    return top_influencers


def get_top_recommendations(influencer_df, nd_sample):
    print(type(nd_sample.tolist()))
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(
        influencer_df['industry_type'] + " " +
        influencer_df['interests'] + " " +
        influencer_df['target_audience_age_range'] + " " +
        influencer_df['target_audience_income_range'] + " " +
        influencer_df['target_audience_gender'] + " " +
        influencer_df['communication_channel'])
    target_audience_vector = tfidf_vectorizer.transform([' '.join(map(str, nd_sample.tolist()))])
    similarity_scores = cosine_similarity(target_audience_vector, tfidf_matrix)
    similarity_scores_for_marketer = similarity_scores[0]
    top_influencer_indices = similarity_scores_for_marketer.argsort()[-5:][::-1]
    top_influencers = influencer_df.iloc[top_influencer_indices]

    return top_influencers


@api_view(['GET'])
def fetch_data_marketers(request, marketer_id):
    influencers, business = get_data_marketers(marketer_id)
    processed = preprocess_data(influencers)
    business_sample = business.fillna('')
    business_sample = business_sample.iloc[0]
    recommendations = get_recommendations(processed, business_sample)
    recommended_influencers = [InfluensysInfluencers.objects.get(id=i) for i in recommendations['id']]
    serializer = InfluencerQuickSerializer(recommended_influencers, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def fetch_data_top_marketers(request, marketer_id):
    influencers, business = get_data_marketers(marketer_id)
    processed = preprocess_data(influencers)
    business_sample = business.fillna('')
    business_sample = business_sample.iloc[0]
    recommendations = get_top_recommendations(processed, business_sample)
    recommended_influencers = [InfluensysInfluencers.objects.get(id=i) for i in recommendations['id']]
    serializer = InfluencerQuickSerializer(recommended_influencers, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def fetch_data_for_campaigns(request, campaign_id):
    influencers, campaign = get_data_campaigns(campaign_id)
    processed = preprocess_data(influencers)
    campaign_sample = campaign.fillna('')
    campaign_sample = campaign_sample.iloc[0]
    recommendations = get_recommendations(processed, campaign_sample)
    recommended_influencers = [InfluensysInfluencers.objects.get(id=i) for i in recommendations['id']]
    serializer = InfluencerQuickSerializer(recommended_influencers, many=True).data
    return Response(serializer, status=status.HTTP_200_OK)
