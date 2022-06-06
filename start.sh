if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/tutanota1/testtiger.git /testtiger
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /testtiger
fi
cd /LUCIFER
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
