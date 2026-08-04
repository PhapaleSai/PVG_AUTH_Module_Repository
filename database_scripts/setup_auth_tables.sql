-- ============================================================
--  AUTH TABLE DDL (Generated from SQLAlchemy Models)
-- ============================================================

CREATE TABLE modules (
	module_id SERIAL NOT NULL, 
	module_name VARCHAR(100) NOT NULL, 
	description VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (module_id)
);

CREATE INDEX ix_modules_module_id ON modules (module_id);

CREATE TABLE roles (
	role_id SERIAL NOT NULL, 
	role_name VARCHAR(100) NOT NULL, 
	description VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	created_by VARCHAR(150), 
	updated_by VARCHAR(150), 
	created_from VARCHAR(100), 
	token_expiry TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (role_id), 
	UNIQUE (role_name)
);

CREATE INDEX ix_roles_role_id ON roles (role_id);

CREATE TABLE users (
	user_id SERIAL NOT NULL, 
	username VARCHAR(100) NOT NULL, 
	full_name VARCHAR(150), 
	email VARCHAR(150) NOT NULL, 
	password_hash VARCHAR(255) NOT NULL, 
	status BOOLEAN, 
	department VARCHAR(100), 
	phone_number VARCHAR(20), 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	created_by VARCHAR(150), 
	updated_by VARCHAR(150), 
	created_from VARCHAR(100), 
	token_expiry TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (user_id), 
	UNIQUE (username)
);

CREATE UNIQUE INDEX ix_users_email ON users (email);

CREATE INDEX ix_users_user_id ON users (user_id);

CREATE TABLE students (
	id SERIAL NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	email VARCHAR(150), 
	phone VARCHAR(15) NOT NULL, 
	username VARCHAR(50) NOT NULL, 
	password_hash VARCHAR(255) NOT NULL, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	created_by VARCHAR(150), 
	updated_by VARCHAR(150), 
	created_from VARCHAR(100), 
	token_expiry TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_students_email ON students (email);

CREATE UNIQUE INDEX ix_students_username ON students (username);

CREATE INDEX ix_students_id ON students (id);

CREATE TABLE features (
	feature_id SERIAL NOT NULL, 
	feature_name VARCHAR(100) NOT NULL, 
	description VARCHAR, 
	module_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (feature_id), 
	FOREIGN KEY(module_id) REFERENCES modules (module_id)
);

CREATE INDEX ix_features_feature_id ON features (feature_id);

CREATE TABLE user_roles (
	user_role_id SERIAL NOT NULL, 
	user_id INTEGER, 
	role_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	created_by VARCHAR(150), 
	updated_by VARCHAR(150), 
	created_from VARCHAR(100), 
	token_expiry TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (user_role_id), 
	FOREIGN KEY(user_id) REFERENCES users (user_id), 
	FOREIGN KEY(role_id) REFERENCES roles (role_id)
);

CREATE INDEX ix_user_roles_user_role_id ON user_roles (user_role_id);

CREATE TABLE user_tokens (
	token_id SERIAL NOT NULL, 
	user_id INTEGER, 
	token VARCHAR NOT NULL, 
	refresh_token VARCHAR, 
	expiry_date TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	refresh_token_expiry TIMESTAMP WITHOUT TIME ZONE, 
	is_active BOOLEAN, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	created_by VARCHAR(150), 
	updated_by VARCHAR(150), 
	created_from VARCHAR(100), 
	token_expiry TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (token_id), 
	FOREIGN KEY(user_id) REFERENCES users (user_id)
);

CREATE UNIQUE INDEX ix_user_tokens_refresh_token ON user_tokens (refresh_token);

CREATE INDEX ix_user_tokens_token_id ON user_tokens (token_id);

CREATE UNIQUE INDEX ix_user_tokens_token ON user_tokens (token);

CREATE TABLE login_log (
	login_log_id SERIAL NOT NULL, 
	user_id INTEGER, 
	ip_address VARCHAR(50), 
	device_info VARCHAR(255), 
	status VARCHAR(50), 
	login_time TIMESTAMP WITHOUT TIME ZONE, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	created_by VARCHAR(150), 
	updated_by VARCHAR(150), 
	created_from VARCHAR(100), 
	token_expiry TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (login_log_id), 
	FOREIGN KEY(user_id) REFERENCES users (user_id)
);

CREATE INDEX ix_login_log_login_log_id ON login_log (login_log_id);

CREATE TABLE permissions (
	permission_id SERIAL NOT NULL, 
	permission_name VARCHAR(150) NOT NULL, 
	action VARCHAR(50), 
	feature_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (permission_id), 
	FOREIGN KEY(feature_id) REFERENCES features (feature_id)
);

CREATE INDEX ix_permissions_permission_id ON permissions (permission_id);

CREATE TABLE role_permissions (
	role_permission_id SERIAL NOT NULL, 
	role_id INTEGER, 
	permission_id INTEGER, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE, 
	PRIMARY KEY (role_permission_id), 
	FOREIGN KEY(role_id) REFERENCES roles (role_id), 
	FOREIGN KEY(permission_id) REFERENCES permissions (permission_id)
);

CREATE INDEX ix_role_permissions_role_permission_id ON role_permissions (role_permission_id);

