SELECT
    -- Reveneue grouping
    DATE_TRUNC('month', pickup_datetime) AS revenue_month,
    VendorID as vendor_id,
    --Note: For BQ use instead: DATE_TRUNC(pickup_datetime, month) AS revenue_month,
    source,

    -- Revenue calculation
    SUM(mta_tax) AS revenue_monthly_mta_tax,
    SUM(tip_amount) AS revenue_monthly_tip_amount,
    SUM(tolls_amount) AS revenue_monthly_tolls_amount,
    SUM(extra) AS revenue_monthly_extra,
    SUM(improvement_surcharge) AS revenue_monthly_improvement_surcharge,
    SUM(total_amount) AS revenue_monthly_total_amount,
    SUM(fare_amount) AS revenue_monthly_fare,
    SUM(congestion_surcharge) AS revenue_monthly_congestion_surcharge,

    -- Additional calculations
    AVG(passenger_count) AS avg_montly_passenger_count,
    AVG(trip_distance) AS avg_montly_trip_distance

    FROM trips
    GROUP BY 1,2,3