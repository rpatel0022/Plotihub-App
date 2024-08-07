"""
URL configuration for plotihub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from property_management_app import views
from plotihub import settings

urlpatterns = [
    path('demo',views.showDemoPage),
    path('signup_admin',views.signup_admin,name="signup_admin"),
    path('signup_tenant',views.signup_tenant,name="signup_tenant"),
    path('signup_staff',views.signup_staff,name="signup_staff"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('do_staff_signup',views.do_staff_signup,name="do_staff_signup"),
    path('do_signup_tenant',views.do_signup_tenant,name="do_signup_tenant"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.ShowLoginPage,name="show_login"),
    # path('get_user_details', views.GetUserDetails),
    # path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    # path('admin_home',HodViews.admin_home,name="admin_home"),
    # path('add_staff',HodViews.add_staff,name="add_staff"),
    # path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    # path('add_course/', HodViews.add_course,name="add_course"),
    # path('add_course_save', HodViews.add_course_save,name="add_course_save"),
    # path('add_tenant', HodViews.add_tenant,name="add_tenant"),
    # path('add_tenant_save', HodViews.add_tenant_save,name="add_tenant_save"),
    # path('add_subject', HodViews.add_subject,name="add_subject"),
    # path('add_subject_save', HodViews.add_subject_save,name="add_subject_save"),
    # path('manage_staff', HodViews.manage_staff,name="manage_staff"),
    # path('manage_tenant', HodViews.manage_tenant,name="manage_tenant"),
    # path('manage_course', HodViews.manage_course,name="manage_course"),
    # path('manage_subject', HodViews.manage_subject,name="manage_subject"),
    # path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    # path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    # path('edit_tenant/<str:tenant_id>', HodViews.edit_tenant,name="edit_tenant"),
    # path('edit_tenant_save', HodViews.edit_tenant_save,name="edit_tenant_save"),
    # path('edit_subject/<str:subject_id>', HodViews.edit_subject,name="edit_subject"),
    # path('edit_subject_save', HodViews.edit_subject_save,name="edit_subject_save"),
    # path('edit_course/<str:course_id>', HodViews.edit_course,name="edit_course"),
    # path('edit_course_save', HodViews.edit_course_save,name="edit_course_save"),
    # path('manage_session', HodViews.manage_session,name="manage_session"),
    # path('add_session_save', HodViews.add_session_save,name="add_session_save"),
    # path('check_email_exist', HodViews.check_email_exist,name="check_email_exist"),
    # path('check_username_exist', HodViews.check_username_exist,name="check_username_exist"),
    # path('tenant_feedback_message', HodViews.tenant_feedback_message,name="tenant_feedback_message"),
    # path('tenant_feedback_message_replied', HodViews.tenant_feedback_message_replied,name="tenant_feedback_message_replied"),
    # path('staff_feedback_message', HodViews.staff_feedback_message,name="staff_feedback_message"),
    # path('staff_feedback_message_replied', HodViews.staff_feedback_message_replied,name="staff_feedback_message_replied"),
    # path('tenant_leave_view', HodViews.tenant_leave_view,name="tenant_leave_view"),
    # path('staff_leave_view', HodViews.staff_leave_view,name="staff_leave_view"),
    # path('tenant_approve_leave/<str:leave_id>', HodViews.tenant_approve_leave,name="tenant_approve_leave"),
    # path('tenant_disapprove_leave/<str:leave_id>', HodViews.tenant_disapprove_leave,name="tenant_disapprove_leave"),
    # path('staff_disapprove_leave/<str:leave_id>', HodViews.staff_disapprove_leave,name="staff_disapprove_leave"),
    # path('staff_approve_leave/<str:leave_id>', HodViews.staff_approve_leave,name="staff_approve_leave"),
    # path('admin_view_attendance', HodViews.admin_view_attendance,name="admin_view_attendance"),
    # path('admin_get_attendance_dates', HodViews.admin_get_attendance_dates,name="admin_get_attendance_dates"),
    # path('admin_get_attendance_tenant', HodViews.admin_get_attendance_tenant,name="admin_get_attendance_tenant"),
    # path('admin_profile', HodViews.admin_profile,name="admin_profile"),
    # path('admin_profile_save', HodViews.admin_profile_save,name="admin_profile_save"),
    # path('admin_send_notification_staff', HodViews.admin_send_notification_staff,name="admin_send_notification_staff"),
    # path('admin_send_notification_tenant', HodViews.admin_send_notification_tenant,name="admin_send_notification_tenant"),
    # path('send_tenant_notification', HodViews.send_tenant_notification,name="send_tenant_notification"),
    # path('send_staff_notification', HodViews.send_staff_notification,name="send_staff_notification"),

    #               #     Staff URL Path
    # path('staff_home', StaffViews.staff_home, name="staff_home"),
    # path('staff_take_attendance', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    # path('staff_update_attendance', StaffViews.staff_update_attendance, name="staff_update_attendance"),
    # path('get_tenants', StaffViews.get_tenants, name="get_tenants"),
    # path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    # path('get_attendance_tenant', StaffViews.get_attendance_tenant, name="get_attendance_tenant"),
    # path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
    # path('save_updateattendance_data', StaffViews.save_updateattendance_data, name="save_updateattendance_data"),
    # path('staff_apply_leave', StaffViews.staff_apply_leave, name="staff_apply_leave"),
    # path('staff_apply_leave_save', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    # path('staff_feedback', StaffViews.staff_feedback, name="staff_feedback"),
    # path('staff_feedback_save', StaffViews.staff_feedback_save, name="staff_feedback_save"),
    # path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
    # path('staff_profile_save', StaffViews.staff_profile_save, name="staff_profile_save"),
    # path('staff_fcmtoken_save', StaffViews.staff_fcmtoken_save, name="staff_fcmtoken_save"),
    # path('staff_all_notification', StaffViews.staff_all_notification, name="staff_all_notification"),
    # path('staff_add_result', StaffViews.staff_add_result, name="staff_add_result"),
    # path('save_tenant_result', StaffViews.save_tenant_result, name="save_tenant_result"),
    # path('edit_tenant_result',EditResultViewClass.as_view(), name="edit_tenant_result"),
    # path('fetch_result_tenant',StaffViews.fetch_result_tenant, name="fetch_result_tenant"),
    # path('start_live_classroom',StaffViews.start_live_classroom, name="start_live_classroom"),
    # path('start_live_classroom_process',StaffViews.start_live_classroom_process, name="start_live_classroom_process"),


    # path('tenant_home', tenantViews.tenant_home, name="tenant_home"),
    # path('tenant_view_attendance', tenantViews.tenant_view_attendance, name="tenant_view_attendance"),
    # path('tenant_view_attendance_post', tenantViews.tenant_view_attendance_post, name="tenant_view_attendance_post"),
    # path('tenant_apply_leave', tenantViews.tenant_apply_leave, name="tenant_apply_leave"),
    # path('tenant_apply_leave_save', tenantViews.tenant_apply_leave_save, name="tenant_apply_leave_save"),
    # path('tenant_feedback', tenantViews.tenant_feedback, name="tenant_feedback"),
    # path('tenant_feedback_save', tenantViews.tenant_feedback_save, name="tenant_feedback_save"),
    # path('tenant_profile', tenantViews.tenant_profile, name="tenant_profile"),
    # path('tenant_profile_save', tenantViews.tenant_profile_save, name="tenant_profile_save"),
    # path('tenant_fcmtoken_save', tenantViews.tenant_fcmtoken_save, name="tenant_fcmtoken_save"),
    # path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
    # path('tenant_all_notification',tenantViews.tenant_all_notification,name="tenant_all_notification"),
    # path('tenant_view_result',tenantViews.tenant_view_result,name="tenant_view_result"),
    # path('join_class_room/<int:subject_id>/<int:session_year_id>',tenantViews.join_class_room,name="join_class_room"),
    # path('node_modules/canvas-designer/widget.html',StaffViews.returnHtmlWidget,name="returnHtmlWidget"),
    path('testurl/',views.Testurl)
]
