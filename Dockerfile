FROM python:latest
COPY /buddy_system_matching.py /buddy_system_matching.py
CMD [ "python", "buddy_system_matching.py" ]
