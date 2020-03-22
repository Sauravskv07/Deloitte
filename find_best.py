import sys 
import pandas as pd
import main as mp
import numpy as np
from keras.models import Model


argumentList = sys.argv 

#print(argumentList)

model = mp.generate_model()

model.load_weights('/home/sauravskv/Desktop/Deloitte/MLSTM-FCN/weights/code__weights.h5')

X= np.zeros((1, 4, 100))

States=['place1','place2','place3','place4','place5','place6','place7','place8','place9','place10','place11','place12','place13','place14','place15','place16','place17','place18','place19','place20','place21','place22','place23','place24','place25','place26','place27','place28']
Markets=['Place0', 'Place1', 'Place2', 'Place3', 'Place4', 'Place5', 'Place6', 'Place7', 'Place8', 'Place9', 'Place10', 'Place11', 'Place12', 'Place13', 'Place14', 'Place15', 'Place16', 'Place17', 'Place18', 'Place19', 'Place20', 'Place21', 'Place22', 'Place23', 'Place24', 'Place25', 'Place26', 'Place27', 'Place28', 'Place29', 'Place30', 'Place31', 'Place32', 'Place33', 'Place34', 'Place35', 'Place36', 'Place37', 'Place38', 'Place39', 'Place40', 'Place41', 'Place42', 'Place43', 'Place44', 'Place45', 'Place46', 'Place47', 'Place48', 'Place49', 'Place50', 'Place51', 'Place52', 'Place53', 'Place54', 'Place55', 'Place56', 'Place57', 'Place58', 'Place59', 'Place60', 'Place61', 'Place62', 'Place63', 'Place64', 'Place65', 'Place66', 'Place67', 'Place68', 'Place69', 'Place70', 'Place71', 'Place72', 'Place73', 'Place74', 'Place75', 'Place76', 'Place77', 'Place78', 'Place79', 'Place80', 'Place81', 'Place82', 'Place83', 'Place84', 'Place85', 'Place86', 'Place87', 'Place88', 'Place89', 'Place90', 'Place91', 'Place92', 'Place93', 'Place94', 'Place95', 'Place96', 'Place97', 'Place98', 'Place99', 'Place100', 'Place101', 'Place102', 'Place103', 'Place104', 'Place105', 'Place106', 'Place107', 'Place108', 'Place109', 'Place110', 'Place111', 'Place112', 'Place113', 'Place114', 'Place115', 'Place116', 'Place117', 'Place118', 'Place119', 'Place120', 'Place121', 'Place122', 'Place123', 'Place124', 'Place125', 'Place126', 'Place127', 'Place128', 'Place129', 'Place130', 'Place131', 'Place132', 'Place133', 'Place134', 'Place135', 'Place136', 'Place137', 'Place138', 'Place139', 'Place140', 'Place141', 'Place142', 'Place143', 'Place144', 'Place145', 'Place146', 'Place147', 'Place148', 'Place149', 'Place150', 'Place151', 'Place152', 'Place153', 'Place154', 'Place155', 'Place156', 'Place157', 'Place158', 'Place159', 'Place160', 'Place161', 'Place162', 'Place163', 'Place164', 'Place165', 'Place166', 'Place167', 'Place168', 'Place169', 'Place170', 'Place171', 'Place172', 'Place173', 'Place174', 'Place175', 'Place176', 'Place177', 'Place178', 'Place179', 'Place180', 'Place181', 'Place182', 'Place183', 'Place184', 'Place185', 'Place186', 'Place187', 'Place188', 'Place189', 'Place190', 'Place191', 'Place192', 'Place193', 'Place194', 'Place195', 'Place196', 'Place197', 'Place198', 'Place199', 'Place200', 'Place201', 'Place202', 'Place203', 'Place204', 'Place205', 'Place206', 'Place207', 'Place208', 'Place209', 'Place210', 'Place211', 'Place212', 'Place213', 'Place214', 'Place215', 'Place216', 'Place217', 'Place218', 'Place219', 'Place220', 'Place221', 'Place222', 'Place223', 'Place224', 'Place225', 'Place226', 'Place227', 'Place228', 'Place229', 'Place230', 'Place231', 'Place232', 'Place233', 'Place234', 'Place235', 'Place236', 'Place237', 'Place238', 'Place239', 'Place240', 'Place241', 'Place242', 'Place243', 'Place244', 'Place245', 'Place246', 'Place247', 'Place248', 'Place249', 'Place250', 'Place251', 'Place252', 'Place253', 'Place254', 'Place255', 'Place256', 'Place257', 'Place258', 'Place259', 'Place260', 'Place261', 'Place262', 'Place263', 'Place264', 'Place265', 'Place266', 'Place267', 'Place268', 'Place269', 'Place270', 'Place271', 'Place272', 'Place273', 'Place274', 'Place275', 'Place276', 'Place277', 'Place278', 'Place279', 'Place280', 'Place281', 'Place282', 'Place283', 'Place284', 'Place285', 'Place286', 'Place287', 'Place288', 'Place289', 'Place290', 'Place291', 'Place292', 'Place293', 'Place294', 'Place295', 'Place296', 'Place297', 'Place298', 'Place299', 'Place300', 'Place301', 'Place302', 'Place303', 'Place304', 'Place305', 'Place306', 'Place307', 'Place308', 'Place309', 'Place310', 'Place311', 'Place312', 'Place313', 'Place314', 'Place315', 'Place316', 'Place317', 'Place318', 'Place319', 'Place320', 'Place321', 'Place322', 'Place323', 'Place324', 'Place325', 'Place326', 'Place327', 'Place328', 'Place329', 'Place330', 'Place331', 'Place332', 'Place333', 'Place334', 'Place335', 'Place336', 'Place337', 'Place338', 'Place339', 'Place340', 'Place341', 'Place342', 'Place343', 'Place344', 'Place345', 'Place346', 'Place347', 'Place348', 'Place349', 'Place350', 'Place351', 'Place352', 'Place353', 'Place354', 'Place355', 'Place356', 'Place357', 'Place358', 'Place359', 'Place360', 'Place361', 'Place362', 'Place363', 'Place364', 'Place365', 'Place366', 'Place367', 'Place368', 'Place369', 'Place370', 'Place371', 'Place372', 'Place373', 'Place374', 'Place375', 'Place376', 'Place377', 'Place378', 'Place379', 'Place380', 'Place381', 'Place382', 'Place383', 'Place384', 'Place385', 'Place386', 'Place387', 'Place388', 'Place389', 'Place390', 'Place391', 'Place392', 'Place393', 'Place394', 'Place395', 'Place396', 'Place397', 'Place398', 'Place399', 'Place400', 'Place401', 'Place402', 'Place403', 'Place404', 'Place405', 'Place406', 'Place407', 'Place408', 'Place409', 'Place410', 'Place411', 'Place412', 'Place413', 'Place414', 'Place415', 'Place416', 'Place417', 'Place418', 'Place419', 'Place420', 'Place421', 'Place422', 'Place423', 'Place424', 'Place425', 'Place426', 'Place427', 'Place428', 'Place429', 'Place430', 'Place431', 'Place432', 'Place433', 'Place434', 'Place435', 'Place436', 'Place437', 'Place438', 'Place439', 'Place440', 'Place441', 'Place442', 'Place443', 'Place444', 'Place445', 'Place446', 'Place447', 'Place448', 'Place449', 'Place450', 'Place451', 'Place452', 'Place453', 'Place454', 'Place455', 'Place456', 'Place457', 'Place458', 'Place459', 'Place460', 'Place461', 'Place462', 'Place463', 'Place464', 'Place465', 'Place466', 'Place467', 'Place468', 'Place469', 'Place470', 'Place471', 'Place472', 'Place473', 'Place474', 'Place475', 'Place476', 'Place477', 'Place478', 'Place479', 'Place480', 'Place481', 'Place482', 'Place483', 'Place484', 'Place485', 'Place486', 'Place487', 'Place488', 'Place489', 'Place490', 'Place491', 'Place492', 'Place493', 'Place494', 'Place495', 'Place496', 'Place497', 'Place498', 'Place499', 'Place500', 'Place501', 'Place502', 'Place503', 'Place504', 'Place505', 'Place506', 'Place507', 'Place508', 'Place509', 'Place510', 'Place511', 'Place512', 'Place513', 'Place514', 'Place515', 'Place516', 'Place517', 'Place518', 'Place519', 'Place520', 'Place521', 'Place522', 'Place523', 'Place524', 'Place525', 'Place526', 'Place527', 'Place528', 'Place529', 'Place530', 'Place531', 'Place532', 'Place533', 'Place534', 'Place535', 'Place536', 'Place537', 'Place538', 'Place539', 'Place540', 'Place541', 'Place542', 'Place543', 'Place544', 'Place545', 'Place546', 'Place547', 'Place548', 'Place549', 'Place550', 'Place551', 'Place552', 'Place553', 'Place554', 'Place555', 'Place556', 'Place557', 'Place558', 'Place559', 'Place560', 'Place561', 'Place562', 'Place563', 'Place564', 'Place565', 'Place566', 'Place567', 'Place568', 'Place569', 'Place570', 'Place571', 'Place572', 'Place573', 'Place574', 'Place575', 'Place576', 'Place577', 'Place578', 'Place579', 'Place580', 'Place581', 'Place582', 'Place583', 'Place584', 'Place585', 'Place586', 'Place587', 'Place588', 'Place589', 'Place590', 'Place591', 'Place592', 'Place593', 'Place594', 'Place595', 'Place596', 'Place597', 'Place598', 'Place599', 'Place600', 'Place601', 'Place602', 'Place603', 'Place604', 'Place605', 'Place606', 'Place607', 'Place608', 'Place609', 'Place610', 'Place611', 'Place612', 'Place613', 'Place614', 'Place615', 'Place616', 'Place617', 'Place618', 'Place619', 'Place620', 'Place621', 'Place622', 'Place623', 'Place624', 'Place625', 'Place626', 'Place627', 'Place628', 'Place629', 'Place630', 'Place631', 'Place632', 'Place633', 'Place634', 'Place635', 'Place636', 'Place637', 'Place638', 'Place639', 'Place640', 'Place641', 'Place642', 'Place643', 'Place644', 'Place645', 'Place646', 'Place647', 'Place648', 'Place649', 'Place650', 'Place651', 'Place652', 'Place653', 'Place654', 'Place655', 'Place656', 'Place657', 'Place658', 'Place659', 'Place660', 'Place661', 'Place662', 'Place663', 'Place664', 'Place665', 'Place666', 'Place667', 'Place668', 'Place669', 'Place670', 'Place671', 'Place672', 'Place673', 'Place674', 'Place675', 'Place676', 'Place677', 'Place678', 'Place679', 'Place680', 'Place681', 'Place682', 'Place683', 'Place684', 'Place685', 'Place686', 'Place687', 'Place688', 'Place689', 'Place690', 'Place691', 'Place692', 'Place693', 'Place694', 'Place695', 'Place696', 'Place697', 'Place698', 'Place699', 'Place700', 'Place701', 'Place702', 'Place703', 'Place704', 'Place705', 'Place706', 'Place707', 'Place708', 'Place709']

count = 0

for state in States:

	for market in Markets:


		if(count==3):
			break

		try:
			df=pd.read_csv("/home/sauravskv/Desktop/Deloitte/MLSTM-FCN/data/csv/Commodity1_price_updated_('"+state+"', '"+market+"', '"+argumentList[3]+"', '"+argumentList[4]+"').csv")

		except:
			continue

		step_count=df.shape[0]

		if(step_count>100):
	
			step_count=100

		X[0, :, :step_count] = df.tail(step_count)[['ModalPrice','MinimumPrice','MaximumPrice','Arrival']].transpose()

		y=model.predict(X)[0]

		if(y[2]>y[1] and y[2]>y[0]):
			count+=1
			print(state,market,y,flush=True)


