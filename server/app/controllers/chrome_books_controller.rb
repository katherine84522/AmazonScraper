class ChromeBooksController < ApplicationController

    def create
        product = ChromeBook.create(name:params[:name], price:params[:price])
        render json: product
    end

    def index
        render json: ChromeBook.all
    end
end
