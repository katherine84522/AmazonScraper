Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
  post "/chrome_books", to: "chrome_books#create"
  get "/chrome_books", to: "chrome_books#index"
end
