CREATE TABLE public.tasks (
	id SERIAL primary key,
	task varchar NULL
);

SELECT id, task
    FROM tasks;

INSERT INTO public.tasks(id, task)
    VALUES
    (1, 'first task'),
    (2, 'second todo thing');
