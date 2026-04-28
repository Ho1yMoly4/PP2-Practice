
-- Add a phone number to an existing contact
CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO phones (contact_id, phone, type)
    SELECT id, p_phone, p_type FROM contacts WHERE name = p_name;
END;
$$;

-- Move contact to a different group (creates the group if it doesn't exist)
CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    g_id INT;
BEGIN
    INSERT INTO groups (name) VALUES (p_group) ON CONFLICT (name) DO NOTHING;
    SELECT id INTO g_id FROM groups WHERE name = p_group;
    UPDATE contacts SET group_id = g_id WHERE name = p_name;
END;
$$;

-- Universal search function (searches across name, email, and phone numbers)
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (c_name VARCHAR, c_email VARCHAR, p_phone VARCHAR) 
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT c.name, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$;