server {
    listen ${LISTEN_PORT};

    location /static {
        alias /app/staticfiles;
    }

    location /media {
        alias /app/media;
    }

    location / {
        proxy_pass      http://${APP_HOST}:${APP_PORT};
        include         /etc/nginx/proxy_params;
    }
}
