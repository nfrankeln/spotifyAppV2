from django.shortcuts import render,redirect
from django.conf import settings
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from requests import Request,post
from .credentials import CLIENT_ID,CLIENT_SECRET,REDIRECT_URI
# Create your views here.

@api_view(['GET'])
def spotify_url(request):

        scopes= """ugc-image-upload
        user-read-playback-state
        user-modify-playback-state
        user-read-currently-playing
        app-remote-control
        playlist-read-private
        playlist-read-collaborative
        playlist-modify-private
        playlist-modify-public
        user-follow-modify
        user-follow-read
        user-read-playback-position
        user-top-read
        user-read-recently-played
        user-library-modify
        user-library-read
        user-read-email
        user-read-private"""
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'show_dialog':True
        }).prepare().url
        return JsonResponse({'url': url})

def spotfiy_callback(request):
        code = request.GET.get('code')
        response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET}).json()

        access_token = response.get('access_token')
        token_type = response.get('token_type')
        refresh_token = response.get('refresh_token')
        expires_in = response.get('expires_in')
        error = response.get('error')
        print(access_token)
        print(refresh_token)
        print(expires_in)
        return redirect('authorization:home')
        pass