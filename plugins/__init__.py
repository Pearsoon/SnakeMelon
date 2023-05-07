import requests
import json

with open("config.json", "r") as f:
    config = json.loads(f.read())


class Robot:
    """定义一个robot的类"""
    plugins = []
    url = config.get("url")
    token = config.get("token")
    wxid = config.get("wxid")

    def __int__(self, url, token, wxid):
        self.url = url
        self.token = token
        self.wxid = wxid

    def add_plugin(self, plugin):
        """添加插件方法"""
        self.plugins.append(plugin)

    def handle_message(self, message):
        """处理消息的函数,用于将消息传入小插件中"""
        for plugin in self.plugins:
            print(plugin)
            plugin.handle(msg=message)

    def change_msg(self, data):
        """格式化msg,将msg转化为json"""
        msg = json.loads(data["content"]["msg"])
        return msg

    def post_(self, data_):
        """post函数,用于触发事件"""
        url = self.url
        response = requests.post(url=url, json=data_)
        return response

    def say(self, to_wxid, msg):
        """通俗易懂,bot说话,目标好友/群/公众号ID"""
        api_ = "SendTextMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "msg": f"{msg}"
        }
        return self.post_(data_)

    def group_msg_at(self, group_wxid, member_wxid, msg):
        """发送群消息并@某个成员"""
        api_ = "SendGroupMsgAndAt"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "member_wxid": f"{member_wxid}",
            "msg": f"{msg}"
        }
        return self.post_(data_)

    def send_msg_at_all(self, group_wxid, msg):
        """发送消息并@全体成员"""
        api_ = "SendMsgAtAll"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "msg": f"{msg}"
        }
        return self.post_(data_)

    def send_image(self, to_wxid, path):
        """发送图片,路径为绝对路径或图床"""
        api_ = "SendimageMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "path": f"{path}"
        }
        return self.post_(data_)

    def send_card(self, to_wxid, member_wxid):
        """发送名片"""
        api_ = "SendCardMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "content": f"{member_wxid}"
        }
        return self.post_(data_)

    def send_msg_record(self, to_wxid, content):
        """发送聊天记录,content为xml代码"""
        api_ = "SendMessageRecord"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "content": f"{content}"
        }
        return self.post_(data_)

    def send_link(self, to_wxid, xml):
        """发送链接消息"""
        api_ = "SendLinkMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "xml": f"{xml}"
        }
        return self.post_(data_)

    def send_share(self, to_wxid, title, desc, image_url, url):
        """发送普通的分享链接,
        链接标题,链接内容,图片地址,跳转地址"""
        api_ = "SendShareLinkMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "title": f"{title}",
            "desc": f"{desc}",
            "image_url": f"{image_url}",
            "url": f"{url}"
        }
        return self.post_(data_)

    def seng_music(self, to_wxid, title, desc, url, dataurl, thumburl):
        """标题,内容,链接地址,mp3地址,http图片地址"""
        api_ = "SendMusicLinkMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "title": f"{title}",
            "desc": f"{desc}",
            "url": f"{url}",
            "dataurl": f"{dataurl}",
            "thumburl": f"{thumburl}"
        }
        return self.post_(data_)

    def send_xml(self, to_wxid, xml):
        """发送小程序"""
        api_ = "SendXmlMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "xml": f"{xml}"
        }
        return self.post_(data_)

    def send_file(self, to_wxid, path):
        """发送文件"""
        api_ = "SendFileMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "path": f"{path}"
        }
        return self.post_(data_)

    def send_video(self, to_wxid, path):
        """发送视频"""
        api_ = "SendVideoMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "path": f"{path}"
        }
        return self.post_(data_)

    def send_emoji(self, to_wxid, path):
        """发送动态表情,本地动态表情文件地址(xxx.gif)"""
        api_ = "SendEmojiMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "path": f"{path}"
        }
        return self.post_(data_)

    def modify_note(self, to_wxid, note):
        """修改好友备注,note为新的备注"""
        api_ = "ModifyFriendNote"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
            "note": f"{note}"
        }
        return self.post_(data_)

    def delete_friend(self, to_wxid):
        """删除好友"""
        api_ = "DeleteFriend"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{to_wxid}",
        }
        return self.post_(data_)

    def agree_friend_verify(self, v1, v2, type_):
        """同意好友请求"""
        api_ = "AgreeFriendVerify"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "v1": f"{v1}",
            "v2": f"{v2}",
            "type": f"{type_}"
        }
        return self.post_(data_)

    def add_friend(self, v1, v2, msg, sance):
        """添加好友,貌似没什么用"""
        api_ = "AddFriendBySearch"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "v1": f"{v1}",
            "v2": f"{v2}",
            "msg": f"{msg}",
            "sance": f"{sance}"
        }
        return self.post_(data_)

    def quit_group(self, group_wxid):
        """退出群聊"""
        api_ = "QuitGroup"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
        }
        return self.post_(data_)

    def accept_transfer(self, from_wxid, payer_pay_id, receiver_pay_id, paysubtype, money):
        """接收转账"""
        api_ = "AccepteTransfer"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "from_wxid": f"{from_wxid}",
            "payer_pay_id": f"{payer_pay_id}",
            "receiver_pay_id": f"{receiver_pay_id}",
            "paysubtype": f"{paysubtype}",
            "money": f"{money}"
        }
        return self.post_(data_)

    def reject_transfer(self, receiver_pay_id):
        """拒收转账"""
        api_ = "RejectTransfer"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "receiver_pay_id": f"{receiver_pay_id}"
        }
        return self.post_(data_)

    def modify_group_name(self, group_wxid, group_name):
        """修改群名称"""
        api_ = "ModifyGroupName"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "group_name": f"{group_name}"
        }
        return self.post_(data_)

    def modify_group_notice(self, group_wxid, notice):
        """修改群公告"""
        api_ = "ModifyGroupNotice"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "Notice": f"{notice}"
        }
        return self.post_(data_)

    def agree_group_invite(self, from_wxid, invite_url):
        """同意入群邀请"""
        api_ = "AgreeGroupInvite"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "from_wxid": f"{from_wxid}",
            "invite_url": f"{invite_url}"
        }
        return self.post_(data_)

    def remove_group_menber(self, group_wxid, member_wxid):
        """踢出群成员"""
        api_ = "RemoveGroupMember"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "member_wxid": f"{member_wxid}"
        }
        return self.post_(data_)

    def on_top(self, wxid):
        """置顶联系人"""
        api_ = "OnTopContact"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{wxid}"
        }
        return self.post_(data_)

    def off_top(self, wxid):
        """取消置顶"""
        api_ = "OffTopContact"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{wxid}"
        }
        return self.post_(data_)

    def on_not_disturb(self, wxid):
        """开启消息免打扰"""
        api_ = "OnNotDisturb"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{wxid}"
        }
        return self.post_(data_)

    def off_not_disturb(self, wxid):
        """关闭消息免打扰"""
        api_ = "OffNotDisturb"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{wxid}"
        }
        return self.post_(data_)

    def invite_by_link(self, group_wxid, friend_wxid):
        """邀请好友入群,通过链接"""
        api_ = "InviteInGroupByLink"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "friend_wxid": f"{friend_wxid}"
        }
        return self.post_(data_)

    def invite(self, group_wxid, friend_wxid):
        """邀请好友入群,直接拉"""
        api_ = "InviteInGroup"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "friend_wxid": f"{friend_wxid}"
        }
        return self.post_(data_)

    def build_group(self, friend_arr):
        """建立新群"""
        api_ = "BuildingGroup"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "friendArr": f"{friend_arr}"
        }
        return self.post_(data_)

    def get_head_image(self, wxid):
        """获取头像"""
        api_ = "GetHeadimgByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def get_name(self, wxid):
        """获取昵称(好友,群聊,公众号)通过缓存"""
        api_ = "GetNameByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def get_note(self, wxid):
        """获取好友备注,通过缓存"""
        api_ = "GetNoteByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def get_chat_num(self, wxid):
        """获取好友微信号,通过缓存"""
        api_ = "GetChatnumByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def get_group_chat_num(self, group_wxid, to_wxid):
        """获取群里的成员微信号,通过缓存"""
        api_ = "GetGroupChatnumByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "to_wxid": f"{to_wxid}",
        }
        return self.post_(data_)

    def get_group_list(self, is_refresh):
        """获取群列表(1为刷新,0为缓存)"""
        api_ = "GetGrouplist"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "is_refresh": f"{is_refresh}"
        }
        return self.post_(data_)

    def get_friend_list(self, is_refresh):
        """获取好友列表(1为刷新,0为缓存)"""
        api_ = "GetFriendlist"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "is_refresh": f"{is_refresh}"
        }
        return self.post_(data_)

    def get_subscription_list(self, is_refresh):
        """获取公众号列表(1为刷新,0为缓存)"""
        api_ = "GetSubscriptionlist"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "is_refresh": f"{is_refresh}"
        }
        return self.post_(data_)

    def search_account(self, content):
        """搜索好友,通过微信号,手机号"""
        api_ = "SearchAccount"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{content}"
        }
        return self.post_(data_)

    def get_info(self, wxid):
        """获取某个好友的详细信息"""
        api_ = "GetDetailInfoByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def get_group_info(self, group_wxid, to_wxid):
        """获取群中用户的详细信息"""
        api_ = "GetGroupMemberDetailInfo"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "to_wxid": f"{to_wxid}",
        }
        return self.post_(data_)

    def get_group_member(self, group_wxid, is_refresh):
        """获取群中的成员列表"""
        api_ = "GetGroupMember"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "is_refresh": f"{is_refresh}",
        }
        return self.post_(data_)

    def get_group_card(self, group_wxid, to_wxid):
        """获取群中用户的详细信息(card)"""
        api_ = "GetGroupcardByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "to_wxid": f"{to_wxid}",
        }
        return self.post_(data_)

    def get_file(self, path):
        """获取文件并返回base64"""
        api_ = "GetFileFoBase64"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "path": f"{path}",
        }
        return self.post_(data_)

    def start(self):
        """启动个人微信"""
        api_ = "StartWeChat"
        data_ = {
            "token": f"{self.token}",
            "api": api_
        }
        return self.post_(data_)

    def exit(self):
        """退出微信"""
        api_ = "ExitWeChat"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def exit_login_win(self):
        """关闭已开启的扫码登陆窗口"""
        api_ = "ExitWeChatLoginWin"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
        }
        return self.post_(data_)

    def restart(self):
        """重启框架"""
        api_ = "RestartFramework"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
        }
        return self.post_(data_)

    def get_moments(self, num):
        """获取朋友圈(1-10)"""
        api_ = "GetMoments"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "num": f"{num}"
        }
        return self.post_(data_)

    def get_moments_for_friend(self, wxid, num):
        """获取指定好友的朋友圈"""
        api_ = "GetMomentsForFriend"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}",
            "num": f"{num}",
        }
        return self.post_(data_)

    def moments_like(self, pyq_id):
        """朋友圈点赞"""
        api_ = "MomentsLike"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "pyq_id": f"{pyq_id}"
        }
        return self.post_(data_)

    def moments_comment(self, pyq_id, msg):
        """朋友圈评论"""
        api_ = "MomentsComment"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "pyq_id": f"{pyq_id}",
            "msg": f"{msg}"
        }
        return self.post_(data_)

    def moments_send(self, pyq_xml):
        """发朋友圈"""
        api_ = "MomentsSend"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "pyq_xml": f"{pyq_xml}"
        }
        return self.post_(data_)

    def contact_save(self, group_wxid):
        """保存到通讯录"""
        api_ = "ContactSave"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}"
        }
        return self.post_(data_)

    def contact_remove(self, group_wxid):
        """移除通讯录"""
        api_ = "ContactRemove"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}"
        }
        return self.post_(data_)

    def open_wechat_browser(self, url):
        """打开微信内置浏览器"""
        api_ = "OpenWeChatBrowser"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "url": f"{url}"
        }
        return self.post_(data_)

    def favorites_list(self):
        """获取收藏列表"""
        api_ = "FavoritesGetList"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def favorites_msg(self, msgid):
        """收藏消息"""
        api_ = "FavoritesMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "msgid": f"{msgid}"
        }
        return self.post_(data_)

    def send_favorites(self, wxid, local_id):
        """发送收藏消息"""
        api_ = "SendFavoritesMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}",
            "local_id": f"{local_id}"
        }
        return self.post_(data_)

    def get_group_notice(self):
        """获取群公告列表"""
        api_ = "GetGroupNoticeList"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def anti_withdraw_on(self):
        """开启防撤回"""
        api_ = "AntiWithdrawON"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def anti_withdraw_off(self):
        """关闭防撤回"""
        api_ = "AntiWithdrawOFF"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def withdraw(self, wxid, msgid):
        """撤回消息"""
        api_ = "WithdrawOwnMessage"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}",
            "msgid": f"{msgid}"
        }
        return self.post_(data_)

    def subscription(self, wxid):
        """关注公众号"""
        api_ = "SubscriptionOfficialAccounts"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def unsubscription(self, wxid):
        """关注公众号"""
        api_ = "UnsubscribeOfficialAccounts"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def speech_to_text(self, msgid):
        """语音转文字"""
        api_ = "SpeechToText"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "msgid": f"{msgid}"
        }
        return self.post_(data_)

    def get_info_by_wxid(self, wxid):
        """通过微信id获取信息"""
        api_ = "GetInfoByWxid"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "wxid": f"{wxid}"
        }
        return self.post_(data_)

    def forward(self, wxid, msgid):
        """转发消息"""
        api_ = "ForwardMsg"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}",
            "msgid": f"{msgid}"
        }
        return self.post_(data_)

    def edit_nickname(self, group_wxid, name):
        """修改自己在群里的昵称"""
        api_ = "SesNicknameInGroup"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "name": f"{name}"
        }
        return self.post_(data_)

    def add_friend_by_group(self, group_wxid, to_wxid, msg):
        """添加群众的成员为好友"""
        api_ = "AddFriendByGroup"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "group_wxid": f"{group_wxid}",
            "to_wxid": f"{to_wxid}",
            "msg": f"{msg}"
        }
        return self.post_(data_)

    def get_invite_info(self, wxid):
        """获取群成员邀请信息"""
        api_ = "GetInviteInInfo"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def set_have_read(self, wxid):
        """设置消息已读"""
        api_ = "SetHaveread"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def get_friends_status(self, wxid):
        """获取好友状态"""
        api_ = "GetFriendsStatus "
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "to_wxid": f"{wxid}"
        }
        return self.post_(data_)

    def clean_chat_history(self):
        """清理聊天记录"""
        api_ = "CleanChathistory "
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def get_runtime(self):
        """获取运行时间"""
        api_ = "GetRuntime "
        data_ = {
            "token": f"{self.token}",
            "api": api_
        }
        return self.post_(data_)

    def get_receive_num(self):
        """获取接收消息数"""
        api_ = "GetWxidRecmsgNum "
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def get_send_num(self):
        """获取发送消息数"""
        api_ = "GetWxidSendmsgNum "
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def get_login_time(self):
        """获取发送消息数"""
        api_ = "GetWxidLogintime "
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}"
        }
        return self.post_(data_)

    def send_moments_link(self, content, title, url, img):
        """发送链接朋友圈
        朋友圈文字标题,链接标题,链接url,图片http地址"""
        api_ = "SendMoments_Like"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{content}",
            "title": f"{title}",
            "url": f"{url}",
            "img": f"{img}"
        }
        return self.post_(data_)

    def send_moments_video(self, content, video):
        """发送链接朋友圈
        朋友圈文字标题,视频仅支持网页视频地址"""
        api_ = "SendMoments_Video"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{content}",
            "video": f"{video}"
        }
        return self.post_(data_)

    def send_moments_img(self, content, img):
        """发送链接朋友圈
        朋友圈文字标题,图片支持网页地址和绝对目录"""
        api_ = "SendMoments_Img"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{content}",
            "img": f"{img}"
        }
        return self.post_(data_)

    def send_moments_str(self, content):
        """发送文本朋友圈"""
        api_ = "SendMoments_Str"
        data_ = {
            "token": f"{self.token}",
            "api": api_,
            "robot_wxid": f"{self.wxid}",
            "content": f"{content}"
        }
        return self.post_(data_)
