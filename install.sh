apt-get update
mkdir ft_userdata
cd ft_userdata/
curl https://raw.githubusercontent.com/freqtrade/freqtrade/stable/docker-compose.yml -o docker-compose.yml
apt install docker.io
docker compose pull
apt install -y docker.io docker-compose-v2
docker compose pull
docker compose run --rm freqtrade create-userdir --userdir user_data
docker compose run --rm freqtrade new-config --config user_data/config.json
docker compose up -d
netstat -nlp
apt install net-tools
netstat -nlp
firewall-cmd --state
apt install firewalld
firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --permanent --zone=public --add-port=443/tcp
firewall-cmd --permanent --zone=public --add-port=3306/tcp
firewall-cmd --permanent --zone=public --add-port=8080/tcp
firewall-cmd --permanent --zone=public --add-port=8081/tcp
firewall-cmd --permanent --zone=public --add-port=8082/tcp
firewall-cmd --reload
firewall-cmd --zone=public --list-ports
netstat -nlp
