/* UP */
CREATE TABLE identity_users (
    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_verified BOOLEAN NOT NULL DEFAULT FALSE,
    role VARCHAR(50) NOT NULL DEFAULT 'user',

    last_login_at DATETIME NULL,
    login_attempts INT NOT NULL DEFAULT 0,
    locked_until DATETIME NULL,

    two_fa_secret VARCHAR(255) NULL,

    provider VARCHAR(50) NULL,
    external_id VARCHAR(255) NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
);

/* DOWN */
DROP TABLE identity_users IF EXISTS;