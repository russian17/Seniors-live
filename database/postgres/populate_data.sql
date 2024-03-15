-- populate_data.sql

-- Insert into Categories
INSERT INTO public."Categories" (category_id, category_name)
VALUES (1, 'Technology');

-- Insert into Seniors
INSERT INTO public."Seniors" (senior_id, senior_fullname, senior_username, senior_password, senior_skills, category_id)
VALUES (1, 'John Doe', 'john_doe', 'securepassword123', 'Software Development', 1);

-- Insert into Youngers
INSERT INTO public."Youngers" (younger_id, younger_fullname, younger_username, younger_password)
VALUES (1, 'Jane Doe', 'jane_doe', 'password123');

-- Insert into Meetings
INSERT INTO public."Meetings" (meeting_id, senior_id)
VALUES (1, 1);

-- Insert into Guests
INSERT INTO public."Guests" (guest_id, younger_id, senior_id, meeting_id)
VALUES (1, 1, 1, 1);
