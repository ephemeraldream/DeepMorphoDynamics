-- Типы цикла, применяемые в системе. В настоящий момент применимы два типа: ICSI и IVF
CREATE TABLE cycle_type
(
    ct_id smallint NOT NULL,						-- Идентификатор типа цикла
    ct_tname character varying(8) NOT NULL,			-- Тип цикла
    CONSTRAINT cycle_type_pk PRIMARY KEY (ct_id)
);


-- Обезличеннная информация о родителях.
CREATE TABLE pair_table
(
    pr_id uuid NOT NULL,							-- Идентификатор пары
    pr_idf uuid NOT NULL,                           -- Идентификатор матери
    pr_idm uuid NOT NULL,                           -- Идентификатор отца
    pt_infertilitytype boolean,                     -- Признак первичного бесплодия матери
    pt_bdatem date NOT NULL,                        -- Дата рождения матери
    pt_bdatef date NOT NULL,                        -- Дата рождения отца
    CONSTRAINT pair_table_pk PRIMARY KEY (pr_id)    
);

-- Линеаризированное дерево маркеров, применённое в системе.
CREATE TABLE marker_tree
(
    mt_id integer NOT NULL,							-- Идентификатор маркера
    mt_parent integer DEFAULT 0,                    -- Родительский маркера
    mt_primary boolean DEFAULT true,                -- 
    mt_stored_data text,                            --
    mt_marker_type integer,                         --
    mt_ins_from decimal(6,2),                       --
    mt_ins_to decimal(6,2),                         --
    mt_stored_data_short text,                      --
    mt_label character varying(10),                 -- Метка для отображения
    CONSTRAINT marker_tree_pkey PRIMARY KEY (mt_id) 
);


--Данные об эмбрионе
CREATE TABLE embryo_data
(
    ed_uuid uuid NOT NULL,                          -- Идентификатор эмбриона
    ed_pr_id uuid NOT NULL,                         -- Идентификатор пары
    ed_id smallint NOT NULL,                        -- Номер лунки
    ed_cs_id uuid NOT NULL,                         -- Идентификатор цикла
    ed_destiny character(4) NOT NULL,               -- Назначение эмбриона (ET - перенос, CRYO - заморозка, DSCR - утилизация)
    ed_mainfocus smallint DEFAULT 0,                -- Базовый фокус при создании
    ed_focus_min smallint,                          -- Нижняя граница фокуса в сериях
    ed_focus_max smallint,                          -- Верхняя граница фокуса в сериях
    ed_own boolean DEFAULT true,                    -- Признак собственного ооцита
    ed_fresh boolean DEFAULT true,                  -- Признак "свежий/размороженный"
    ed_biodate date,                                -- Дата биопсии
    ed_fertilization smallint,                      -- Количество пронуклеусов при оплодотворении
    ed_seriescount integer DEFAULT 0,               -- Количество серий изображений
    ed_pn_size_rate character varying(6),           -- Соотношение размеров пронуклеусов
    ed_insemination timestamp without time zone,	-- Дата и время инсеминации (оплодотворения)
    ed_iceps boolean DEFAULT false,					-- Признак наличия неоднородности цитоплазмы (ЭПС)
    ed_icinc boolean DEFAULT false,                 -- Признак наличия неоднородности цитоплазмы (прочие включения)
    ed_anom_form boolean DEFAULT false,             -- Признак наличия аномальной формы
    ed_cl2_sz boolean DEFAULT false,                -- Признак равномерности бластомеров после деления на 2 клетки
    ed_cl3_sz boolean DEFAULT false,                -- Признак равномерности бластомеров после деления на 3 клетки
    ed_cl4_sz boolean DEFAULT false,                -- Признак равномерности бластомеров после деления на 4 клетки
    ed_cl5_sz boolean DEFAULT false,                -- Признак равномерности бластомеров после деления на 5 клетки
    ed_cl6_sz boolean DEFAULT false,                -- Признак равномерности бластомеров после деления на 6 клетки
    ed_cl8_sz boolean DEFAULT false,                -- Признак равномерности бластомеров после деления на 8 клетки
    ed_clrev boolean DEFAULT false,                 -- Признак наличия реверсивного дробления
    ed_mnb boolean DEFAULT false,                   -- Признак наличия мультинуклеации
    ed_vacuolization boolean DEFAULT false,         -- Признак наличия вакуолизации
    ed_frag integer,                                -- Процент фрагментации (0 - 100)
    ed_ins_method smallint DEFAULT 1,               -- Метод инсеминации (cycle_type)
    ed_finalscore character varying(3),             -- Финальная оценка эмбриона по Гарднеру
    ed_pn_start_time decimal(6,2),                  -- Время образования пронуклеусов
    ed_pn_ds_time decimal(6,2),                     -- Время исчезновения пронуклеусов
    ed_t2 decimal(6,2),                             -- Время деления на 2 бластомера (часов от инсеминации)
    ed_t3 decimal(6,2),                             -- Время деления на 3 бластомера (часов от инсеминации)
    ed_t4 decimal(6,2),                             -- Время деления на 4 бластомера (часов от инсеминации)
    ed_t5 decimal(6,2),                             -- Время деления на 5 бластомера (часов от инсеминации)
    ed_t6 decimal(6,2),                             -- Время деления на 6 бластомера (часов от инсеминации)
    ed_t8 decimal(6,2),                             -- Время деления на 8 бластомера (часов от инсеминации)
    ed_first_clvg_time decimal(6,2),                -- Время первого деления (min(ed_t2..ed_t8))
    ed_compact_start decimal(6,2),                  -- Время начала компактизации
    ed_compacted_time decimal(6,2),                 -- Время завершения компактизации
    ed_cavitation_start decimal(6,2),               -- Время начала кавитации
    ed_full_blast decimal(6,2),                     -- Время образования полной бластоцисты
    ed_expand_time decimal(6,2),                    -- Время образования экспандированной бластоцисты
    ed_hatching_start decimal(6,2),                 -- Время начала хэтчинга
    et_etdt timestamp without time zone,            -- Дата и время переноса
    et_cat uuid,                                    -- Катетер переноса
    et_frzdt timestamp without time zone,           -- Дата и время заморозки
    et_dscrdt timestamp without time zone,          -- Дата и время утилизации
    et_etwith uuid,                                 -- Идентификатор эмбриона, перенесённого с данным (при двойном переносе)
    et_hcgtest boolean DEFAULT false,               -- ХГЧ тест положителен (наступление биохимической беременности)
    et_cp boolean DEFAULT false,                    -- Наступление клинической беременности (определимой по УЗИ)
    et_gstsacs integer DEFAULT 0,                   -- Количество плодов по УЗИ
    et_prresult integer,                            -- Результат беременности
    et_brthdate timestamp without time zone,        -- Дата рождения
    et_nbqtty integer,                              -- Количество новорожденных
    et_nbweight integer,                            -- Вес новорожденного
    vcs_srvrserial character varying(255),          -- Серийный номер прибора
    vcs_scale real,                                 -- Масштаб видеокамеры прибора (точек/миктометр)
    CONSTRAINT et_data_pk PRIMARY KEY (ed_uuid)
);

--Данные по серии изображений
CREATE TABLE well_timeline
(
    wtl_id integer NOT NULL,						    -- Идентификатор (номер) серии
    wtl_ed_uuid uuid NOT NULL,                          -- Идентификатор эмбриона
    wtl_focus smallint DEFAULT 0,                       -- Главная фокальная плоскость в серии
    wtl_tempr real NOT NULL,                            -- Температура камеры культивирования
    wtl_gas_co2 character varying NOT NULL,             -- Данные по CO2 в камере культивирования
    wtl_co2_concentration real,                         -- Концентрация CO2 в камере культивирования
    wtl_co2_flow real,                                  -- Газовый поток CO2 в камере культивирования
    wtl_frame_dt timestamp without time zone NOT NULL,	-- Дата и время получения кадра 
    CONSTRAINT well_tl_pk PRIMARY KEY (wtl_id, wtl_ed_uuid),
    CONSTRAINT embryo_data_well_timeline_fk FOREIGN KEY (wtl_ed_uuid)
        REFERENCES embryo_data (ed_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Кадры серии изображений
CREATE TABLE well_timeline_frames
(
    wtf_wtl_id integer NOT NULL,						-- Идентификатор (номер) серии
    wtf_ed_uuid uuid NOT NULL,                          -- Идентификатор эмбриона
    wtf_rel_focus integer NOT NULL,                     -- Относительная фокальная плоскость
    wtf_frame blob NOT NULL,                            -- Кадр (bmp)
    wtf_dif integer DEFAULT 0,                          -- Разница с предыдущим кадром
    wtf_stabilized boolean NOT NULL DEFAULT false,      -- Признак выполнения стабилизации
    CONSTRAINT well_timeline_frames_pk PRIMARY KEY (wtf_wtl_id, wtf_ed_uuid, wtf_rel_focus),
    CONSTRAINT well_timeline_well_timeline_frames_fk FOREIGN KEY (wtf_ed_uuid, wtf_wtl_id)
        REFERENCES well_timeline (wtl_ed_uuid, wtl_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Маркеры кадра
CREATE TABLE well_timeline_marker
(
    wtm_wtl_id integer NOT NULL,					-- Идентификатор (номер) серии
    wtm_focus smallint NOT NULL,                    -- Относительная фокальная плоскость
    wtm_ed_uuid uuid NOT NULL,                      -- Идентификатор эмбриона
    wtm_mark_id integer NOT NULL,					-- Идентификатор маркера
    wtm_mark_data text,								-- Служебные данные маркера
    wtm_restrict_mark integer NOT NULL,				-- Метка ограничения
    CONSTRAINT well_timeline_marker_pkey PRIMARY KEY (wtm_wtl_id, wtm_focus, wtm_ed_uuid, wtm_mark_id)
);

-- Разметка главной фокальной плоскости эмбриона
CREATE TABLE embryo_focus
(
    ef_ed_uuid uuid NOT NULL,						-- Идентификатор эмбриона
    ef_focus smallint NOT NULL,                     -- Главная фокальная плоскость
    ef_wtl_id integer NOT NULL,                     -- Идентификатор (номер) серии применения данной главной плоскости
    CONSTRAINT ef_pk PRIMARY KEY (ef_ed_uuid, ef_wtl_id),
    CONSTRAINT embryo_data_embryo_focus_fk FOREIGN KEY (ef_ed_uuid)
        REFERENCES embryo_data (ed_uuid) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
