# 🧩 System Architecture Diagram

```plaintext
                         +------------------+
                         |   Reddit API     |
                         +--------+---------+
                                  |
                                  ↓ (PRAW)
                      +--------------------------+
                      |   Flask Backend (Python) |
                      +--------------------------+
                            |    |      |
                            ↓    ↓      ↓
       +------------------+   +------------+   +---------------------+
       | Sentiment Module |   | Topic Logic|   | Gemini Story Engine |
       +------------------+   +------------+   +---------------------+
                            ↓
                  +------------------------+
                  |   REST API Endpoints   |
                  +-----------+------------+
                              ↓
                +-------------------------------+
                |     React Frontend (UI)       |
                +-------------------------------+
                         |    |    |     |
                         ↓    ↓    ↓     ↓
                 Dashboard  Topics  Stories  References
