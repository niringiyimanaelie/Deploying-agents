SELECT
    up.user_id_hex,
    m.date_utc,
    COUNT_IF(m2.time_in_app_mins_per_day > 1) AS active_days_in_7d
FROM dev.data_science.metrics_daily_userlevel_app_time_sessions m
JOIN dev.data_science.user_profiles up 
      ON m.username = up.latest_username
LEFT JOIN dev.data_science.metrics_daily_userlevel_app_time_sessions m2
      ON m2.username = m.username
     AND m2.date_utc > m.date_utc
     AND m2.date_utc <= DATEADD(day, 7, m.date_utc)
GROUP BY up.user_id_hex, m.date_utc
ORDER BY up.user_id_hex, m.date_utc;
