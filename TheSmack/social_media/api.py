@api.route('/get_recent_emotion/<query_user>', methods=['GET'])
def get_user(query_user):
    for user in User.query.filter_by(username=query_user):
        re = user.recent_emotion[0]
        return jsonify({'username': user.username, 'recent_emotion': {
            'date_added': re.date_added,
            'condition': re.condition,
            'temp': re.temp,
            'desc': re.desc,
        }})
    return 'Request failed, make sure user exists (case sensitive).', 404

@api.route('/all_users', methods=["GET"])
def all_users():
    user_list = User.query.all()
    users = []
    for user in user_list:
        users.append({'id': user.id, 'name': user.username})
    response = jsonify({'all_users': users})
    return response, 200

@api.route('/all_recent_emotions', methods=["GET"])
def are():
    re_list = RecentEmotion.query.all()
    re = []
    for res in re_list:
        re.append({'id': res.id, 'owner_id': res.user_id, 'condition': res.condition, 'temp': res.temp})
        response = jsonify({'all_recent_emotions': re})
        return response, 200