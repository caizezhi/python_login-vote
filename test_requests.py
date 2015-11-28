# -*- coding:utf-8 -*-
import requests
import json
import re
import user


def test_login(username, pwd, i):
	s = requests.session()

	data = {'gUser.loginName': username, 'gUser.password': pwd}
	res = s.post('http://uzone.univs.cn/sso.action', data)
	url = s.get('http://mzml.univs.cn:8081/common/checkcode')
	jstring = json.loads(url.text)
	token = jstring['data']['date']
	checkcode = jstring['data']['checkout']
	subSiteId = jstring['data']['subSiteId']
	checklogin = "http://uzone.univs.cn/checkSSOLogin.action?token=" + token + "&subSiteId=" + subSiteId + "&checkCode=" + checkcode + "&returnUrl=http://mzml.univs.cn:8081/land.html"
	newcode = s.get(checklogin, allow_redirects=False).headers
	newcheckcode = newcode['location']
	loginurl = newcheckcode
	newcheckcode = re.search(r"=\b.*\b&\b", str(newcheckcode)).group().strip('=').strip('&')
	uid = re.search(r"d=\b.*\b", str(loginurl)).group().strip('d=')
	s.get(loginurl)
	signinurl = "http://mzml.univs.cn:8081/user/sigin"
	signdata = {'checkcode': newcheckcode, "uid": uid, "token": token}
	signin = s.post(signinurl, signdata)
	voteurl = "http://mzml.univs.cn:8081/user/addvote"
	votedata1 = {'type': 1, 'id': 193}
	votedata2 = {'type': 1, 'id': 195}
	votedata3 = {'type': 2, 'id': 138}
	votedata4 = {'type': 2, 'id': 139}
	vote1 = s.post(voteurl, votedata1)
	vote2 = s.post(voteurl, votedata2)
	vote3 = s.post(voteurl, votedata3)
	vote4 = s.post(voteurl, votedata4)
	print signin.text
	print vote1.text
	print vote2.text
	print vote3.text
	print vote4.text
	print i
for i in range(1400, 2605):
	try:
		test_login(user.user[i]['user'], str(user.user[i]['pwd']), i)
	except:
		print i