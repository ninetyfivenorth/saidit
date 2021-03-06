## The contents of this file are subject to the Common Public Attribution
## License Version 1.0. (the "License"); you may not use this file except in
## compliance with the License. You may obtain a copy of the License at
## http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
## License Version 1.1, but Sections 14 and 15 have been added to cover use of
## software over a computer network and provide for limited attribution for the
## Original Developer. In addition, Exhibit A has been modified to be
## consistent with Exhibit B.
##
## Software distributed under the License is distributed on an "AS IS" basis,
## WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
## the specific language governing rights and limitations under the License.
##
## The Original Code is reddit.
##
## The Original Developer is the Initial Developer.  The Initial Developer of
## the Original Code is reddit Inc.
##
## All portions of the code written by reddit are Copyright (c) 2006-2015
## reddit Inc. All Rights Reserved.
###############################################################################

<%namespace file="printablebuttons.m" import="ynbutton"/>

<%!
    from r2.models import FlairTemplate, USER_FLAIR, LINK_FLAIR
    from r2.lib.pages.pages import FlairTemplateEditor

    empty_template = FlairTemplate()
    empty_template._committed = True  # to disable unnecessary warning
%>

<div class="flairlist usertable">
  <div class="flairrow">
    <span class="header tagline">&nbsp;</span>
    <span class="header narrow">${_('user can edit?')}</span>
    <span class="header">${_('flair text')}</span>
    <span class="header">${_('css class')}</span>
  </div>
  <div class="flairtemplatelist flairlist pretty-form">
    %for flair_template in thing.templates:
      ${flair_template}
    %endfor

    <%
    if thing.flair_type == USER_FLAIR:
        empty_id = 'empty-user-flair-template'
    elif thing.flair_type == LINK_FLAIR:
        empty_id = 'empty-link-flair-template'
    %>
    <div id="${empty_id}">
      ${FlairTemplateEditor(empty_template, thing.flair_type)}
    </div>
  </div>
  ${ynbutton(_("clear all flair templates"), _("cleared"),
             "clearflairtemplates",
             hidden_data=dict(flair_type=thing.flair_type))}
</div>
