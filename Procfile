# upload your SSH key to Heroku (if not already done)
heroku keys:add ~/.ssh/id_ed25519.pub

# create the app in the EU region
heroku create APP_NAME --ssh-git --region eu

# you should see the origin remote for GitHub
# and the heroku remote for Heroku
git remote -v

# manually add the heroku remote if necessary
git remote add heroku https://git.heroku.com/APP_NAME.git

# deploy the app
git push heroku master

# start the web dyno
heroku ps:scale web=1

# check the logs for errors
heroku logs --tail
