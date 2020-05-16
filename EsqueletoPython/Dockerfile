FROM python
WORKDIR /code/

RUN pip3 install --upgrade pip
RUN pip3 install nose
RUN pip3 install nose-cov
RUN pip3 install pandas
RUN pip3 install requests
RUN pip3 install pycryptodome
RUN pip3 install rednose
RUN pip3 install pytest
RUN pip3 install pytest-cov
RUN pip3 install mock
RUN pip3 install pymongo


EXPOSE 5000

ADD . /code/
COPY . /code/
ENV KEY_RAPID="55925beedbmsh27ae8d9327146f4p145768jsn71121cc81910"


#CMD nosetests  --with-coverage
CMD nosetests -sv --rednose
CMD python -m unittest test.create_table_test
