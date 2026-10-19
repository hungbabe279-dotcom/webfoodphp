FROM php:8.0-apache

# Cài đặt extension mysqli và pdo_mysql cho PHP
RUN docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable mysqli

# Bật mod_rewrite
RUN a2enmod rewrite

WORKDIR /var/www/html
