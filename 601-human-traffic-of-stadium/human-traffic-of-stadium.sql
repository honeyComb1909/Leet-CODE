SELECT s.*
FROM Stadium s
WHERE s.people >= 100
  AND (
        (
            EXISTS (
                SELECT 1
                FROM Stadium s1
                WHERE s1.id = s.id + 1
                  AND s1.people >= 100
            )
            AND EXISTS (
                SELECT 1
                FROM Stadium s2
                WHERE s2.id = s.id + 2
                  AND s2.people >= 100
            )
        )
        OR
        (
            EXISTS (
                SELECT 1
                FROM Stadium s1
                WHERE s1.id = s.id - 1
                  AND s1.people >= 100
            )
            AND EXISTS (
                SELECT 1
                FROM Stadium s2
                WHERE s2.id = s.id + 1
                  AND s2.people >= 100
            )
        )
        OR
        (
            EXISTS (
                SELECT 1
                FROM Stadium s1
                WHERE s1.id = s.id - 1
                  AND s1.people >= 100
            )
            AND EXISTS (
                SELECT 1
                FROM Stadium s2
                WHERE s2.id = s.id - 2
                  AND s2.people >= 100
            )
        )
      )
ORDER BY s.visit_date;