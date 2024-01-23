set -e

TAXI_TYPES=("yellow" "green")
YEAR=2020

# https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-09.parquet
# https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2023-09.parquet

URL_PREFIX="https://d37ci6vzurychx.cloudfront.net/trip-data"
for TAXI_TYPE in ${TAXI_TYPES[@]}; do
    echo "Scraping ${TAXI_TYPE} data for ${YEAR}"
    for MONTH in {1..12}; do

        FMONTH=`printf "%02d" ${MONTH}`

        URL="${URL_PREFIX}/${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.parquet"
        echo $URL
        LOCAL_PREFIX="data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"
        LOCAL_FILE="${TAXI_TYPE}_tripdata_${YEAR}_${FMONTH}.parquet"
        LOCAL_PATH="${LOCAL_PREFIX}/${LOCAL_FILE}"

        echo "downloading ${URL} to ${LOCAL_PATH}"
        mkdir -p ${LOCAL_PREFIX}
        wget ${URL} -O ${LOCAL_PATH}

    done
done