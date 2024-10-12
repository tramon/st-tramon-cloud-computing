CREATE TABLE public.status (
	id SERIAL PRIMARY KEY,
	status varchar NULL
);

INSERT INTO public.status (id, status)
    VALUES
    (1, 'to do'),
    (2, 'in progress'),
    (3, 'done');

CREATE TABLE public.tasks (
    id SERIAL PRIMARY KEY,
    task VARCHAR NULL,
    status_id INTEGER
        CONSTRAINT fk_status_id
        REFERENCES public.status(id)
);

INSERT INTO public.tasks (task, status_id)
    VALUES
    ('first task', 1),
    ('second todo thing', 2),
    ('done task', 3);


SELECT id, task, status_id FROM tasks;
SELECT id, status  FROM status;
SELECT * FROM tasks ORDER BY id FETCH FIRST 100 ROWS WITH ties
SELECT * FROM status ORDER BY id FETCH FIRST 100 ROWS WITH ties

SELECT
    t.id,
    t.task, 
    s.status
FROM
    public.tasks t
JOIN
    public.status s ON t.status_id = s.id
ORDER BY
    t.id
FETCH FIRST 100 ROWS WITH TIES;
