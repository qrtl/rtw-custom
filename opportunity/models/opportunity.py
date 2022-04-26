# -*- coding: utf-8 -*-

from odoo import models, fields, api


class opportunity(models.Model):
    _name = 'opportunity.stage'
    _description = 'opportunity stage'

    accounts = fields.Many2one('res.partner', "Account", copy=False)  # アカウント
    name = fields.Char('Name')  # 名称 E列
    Description = fields.Text('Description')  # 説明 F列
    stage_name = fields.Char('StageName')  # 段階名 G列
    stage_sort_order = fields.Integer('StageSortOrder')  # 受注段階コード H列
    amount = fields.Float('Amount')  # 金額 I列
    probability = fields.Integer('Probability')  # 確率 J列
    expected_revenue = fields.Float('ExpectedRevenue')  # 予想売上高 K列
    # total_opportunity_quantity = fields.Float('TotalOpportunityQuantity')  # 契約金額合計 L列
    close_date = fields.Datetime('CloseDate')  # 完了日 M列
    type = fields.Char('Type')  # N列
    nextstep = fields.Char('NextStep')  # 次の段階 O列
    lead_source = fields.Char('LeadSource')  # 見込み顧客の獲得方法 P列
    isclosed = fields.Boolean('IsClosed')  # 完了済みフラグ Q列
    is_won = fields.Boolean('IsWon')  # 成約フラグ R列
    forecast_category = fields.Char('ForecastCategory')  # 予測カテゴリ S列
    forecast_category_name = fields.Char('ForecastCategoryName')  # 予測カテゴリ名 T列
    campaign_id = fields.Char('CampaignId')  # キャンペーンId U列
    # has_opportunity_line_item = fields.Char('HasOpportunityLineItem')  # 段階名 V列
    # price_book2_id = fields.Char('Pricebook2Id')  # 段階名 W列
    owner_id = fields.Char('OwnerId')  # 所有者Id X列
    created_date = fields.Datetime('CreatedDate')  # 作成日 Y列
    created_by_id = fields.Char('CreatedById')  # 作成ID Z列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日
    last_modified_by_id = fields.Char('LastModifiedById')  # 最終更新者
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日
    last_activity_date = fields.Datetime('LastActivityDate')  # システム最終活動日
    last_stage_change_date = fields.Datetime('LastStageChangeDate')  # 最終ステージ変更日
    fiscal_year = fields.Integer('FiscalYear')  # 会計年度
    fiscal_quarter = fields.Integer('FiscalQuarter')  # 会計四半期
    # contact_id = fields.Char('ContactId')  # コンタクトId
    primary_partner_Account_id = fields.Char('PrimaryPartnerAccountId')  # プライマリーパートナーId
    # synced_quote_id = fields.Char('SyncedQuoteId')  # 同期引用Id
    # contract_id = fields.Char('ContractId')  # 契約Id
    last_amount_changed_history_id = fields.Char('LastAmountChangedHistoryId')  # 最終金額変更履歴
    last_close_date_changed_history_id = fields.Char('LastCloseDateChangedHistoryId')  # 最終完了日変更履歴
    progress_check_date = fields.Datetime('Field1__c')  # 進捗確認日 AN列
    quote_number_by_hukusuke = fields.Char('Field2__c')  # 福助で採番される見積番号 AO列
    quote_number = fields.Char('Field3_del__c')  # 見積番号 AP列
    previous_amount = fields.Float('previousamount__c')  # 直前の金額 AQ列
    opportunity_number = fields.Char('Field4__c')  # 商談番号 AR列
    last_amount_change_datetime = fields.Datetime('lastamountchangedatetime__c')  # 最終金額変更日時 AS列
    presentation = fields.Integer('presentation__c')  # 通常プレゼン AT列 ★0，1，空白あり
    project_details = fields.Text('Field60__c')  # 案件詳細 AU列
    Determined_on_the_day = fields.Integer('Determinedontheday__c')  # 当日確定 AV列 ★0，1，空白あり
    delivery_date_unknown = fields.Integer('Field5__c')  # 納期不明 AW列 ★0，1，空白あり
    delivery_type = fields.Char('Field6__c')  # 納入先種別 AX列
    order_amount = fields.Float('Field7__c')  # 受注額 AY列
    omotesando_visit = fields.Integer('Field87__c')  # 表参道来店 AZ列 ★0，1，空白あり
    fair = fields.Char('Field22__c')  # Fair BA列
    million_amount = fields.Integer('X100_amount__c')  # 100万金額 BB列
    million_order_amount = fields.Integer('X100_amount_a__c')  # 100万受注額 BC列
    competition_a = fields.Char('Field16__c')  # 競合A BD列
    fair_advance_plan = fields.Integer('Field34_plan__c')  # フェア事前プラン BE列 ★0，1，空白あり
    product_others = fields.Char('Field14__c')  # 商品その他（補足） BF列
    our_strengths = fields.Text('Field30__c')  # 自社の強み BG列
    million_order_count = fields.Integer('X100_count_a__c')  # 100万受注数 BH列 ★0，1，空白あり
    total_million_order_count = fields.Integer('X100_count__c')  # 100万総数 BI列 ★0，1，空白あり
    Use_Purpose = fields.Text('Field61__c')  # 使用用途(その他） BJ列
    reason_selection = fields.Text('Field62__c')  # 選定理由 BK列
    Use_Purpose1 = fields.Char('Field63_purpose__c')  # 使用用途① BL列
    Use_Purpose2 = fields.Char('Field64_purpose__c')  # 使用用途② BM列
    Use_Purpose3 = fields.Char('Field65_purpose__c')  # 使用用途③ BN列
    other = fields.Integer('ITEM_other_08__c')  # その他 BO列 ★0，1，空白あり
    ac = fields.Integer('CHAI_2__c')  # AC BP列 ★0，空白あり
    website = fields.Char('WEB__c')  # WEBサイト BQ列
    competitive_reason = fields.Text('Field31__c')  # 競合理由 BR列
    order_no = fields.Char('NO__c')  # 受注NO BS列
    facility_name = fields.Char('Field64__c')  # 施設名 BT列
    competition_other = fields.Char('Field17__c')  # 競合（その他） BU列
    competitive_product_d = fields.Char('Field18__c')  # 競合商品(D) BV列
    competitive_product_name = fields.Char('Field19__c')  # 競合商品名 BW列
    competitive_product_l = fields.Char('L__c')  # 競合商品(L) BX列
    competitive_product_other = fields.Char('Field20__c')  # 競合商品（他） BY列
    other_strengths = fields.Text('Field21__c')  # 他社の強み BZ列
    competition_b = fields.Char('B__c')  # 競合B CA列
    campaign = fields.Char('Field65__c')  # キャンペーン CB列
    product_list_other = fields.Char('Field68__c')  # 商品リスト（その他） CC列
    action1 = fields.Char('Field23__c')  # アクション① CD列
    memo = fields.Text('Field35_del__c')  # メモ CE列
    branch = fields.Char('Branch__c')  # Branch CF列
    action2 = fields.Char('Field24__c')  # アクション② CG列
    last_event_comment = fields.Text('LastEventComment__c')  # 最終行動コメント CH列
    diana = fields.Integer('DIANA__c')  # DIANA台数 CI列
    sample_sale = fields.Char('Field25__c')  # サンプル販売 CJ列
    sample_sales_amount = fields.Integer('Field26__c')  # サンプル販売金額 CK列
    push_c = fields.Integer('Push_Counter__c')  # Push C(完了予定日を翌月以降に変更した回数をカウント) CL列
    area = fields.Char('Field32_del__c')  # エリア CM列
    pre_contract_presentation = fields.Integer('Field34_plan2__c')  # 契約前プレゼン CN列
    overlap = fields.Char('Field34__c')  # Overlap CO列
    memo_other = fields.Char('Field28__c')  # メモ（台数など） CP列
    product_list_rug = fields.Char('Field70__c')  # 商品リスト（ラグ） CQ列
    product_list_dt2 = fields.Char('Dt2__c')  # 商品リスト(Dt2) CR列
    product_list_dt1 = fields.Char('Dt1__c')  # 商品リスト(Dt1) CS列
    product_list_lt2 = fields.Char('Lt2__c')  # 商品リスト(Lt2) CT列
    fair_Year = fields.Datetime('Field33__c')  # フェア開催年 CU列
    product_list_lt1 = fields.Char('Lt1__c')  # 商品リスト(Lt1) CV列
    product_list_ec1 = fields.Char('EC1__c')  # 商品リスト(EC1) CW列
    product_list_ec2 = fields.Char('EC2_2__c')  # 商品リスト(EC2) CX列
    l_set = fields.Integer('Lset__c')  # Lセット CY列
    product_list_st2 = fields.Char('St2__c')  # 商品リスト(St2) CZ列
    product_list_st1 = fields.Char('St1__c')  # 商品リスト(St1) DA列
    opportunity_completion_date = fields.Datetime('Field72__c')  # 商談完了日 DB列



#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
