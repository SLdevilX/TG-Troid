# lasiya
FROM programmingerror/ultroid:v0.0.1

RUN git clone https://github.com/SLdevilX/TG-Troid.git /root/TG-Troid/

RUN git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me
WORKDIR /root/TG-Troid/

RUN pip3 install -r requirements.txt
RUN npm install -g npm@7.11.2 -g
RUN npm install
RUN npm run build
