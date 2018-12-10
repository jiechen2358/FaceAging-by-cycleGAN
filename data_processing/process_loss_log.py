import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# TITLE = 'CycleGAN Model with CACD Data'
# LOSS_LOG_FILE = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/checkpoints/young2old_large_2_cyclegan/loss_log.txt'

# TITLE = 'horse2zebra CycleGAN Model'
# LOSS_LOG_FILE = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/checkpoints/horse2zebra_cyclegan/loss_log.txt'

# TITLE = 'CycleGAN Model with Transfer Learning'
# LOSS_LOG_FILE = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/checkpoints/young2old_transfer/loss_log.txt'

# TITLE = 'CycleGAN Model with Fine Tuning'
# LOSS_LOG_FILE = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/checkpoints/young2old_fine_tune/loss_log.txt'
 
# TITLE = 'CycleGAN Model with Mixed Gender Images'
# LOSS_LOG_FILE = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/trained_model/wiki_mix_male_female/loss_log.txt'

# TITLE = 'CycleGAN Mopdel with Male Images'
# LOSS_LOG_FILE = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/trained_model/wiki_all_male/loss_log.txt'

# TITLE = 'CycleGAN Model with Female Images'
# LOSS_LOG_FILE = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/trained_model/wiki_all_female/loss_log.txt'

TO_FIX = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/trained_model/wiki_all_male/to_fix.txt'
FIXED = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/trained_model/wiki_all_male/fixed.txt'

TITLE_MAP = {
	'D_A': 'Discriminator A',
	'D_B': 'Discriminator B',
	'G_A': 'Generator A',
	'G_B': 'Generator B',
	'cycle_A': 'Cycle Consistency A',
	'cycle_B': 'Cycle Consistency B',
}


def parseDictString(line):
	result = {}
	parts = line.split(' ')
	for i in range(0, len(parts), 2):
		key = parts[i].replace(':', '').strip()
		value = parts[i + 1].strip()
		if '.' in value:
			value = float(parts[i + 1].strip())
		else:
			value = int(parts[i + 1].strip())
		result[key] = value
	return result


def parseLossLogFile(log_file_path):
	with open(log_file_path) as loss_log:
		raw_loss_log = loss_log.readlines()
	content = [x.strip() for x in raw_loss_log if not x.startswith('===')]
	epoch_iters_map = {}
	result = {}
	for line in content:
		metadata = parseDictString(line[line.find("(") + 1 : line.find(")")].replace(',', '').strip())
		data = parseDictString(line[line.find(")") + 2 :].strip())
		epoch = metadata['epoch']
		iters = metadata['iters']
		if not epoch in epoch_iters_map or epoch_iters_map[epoch] < iters:
			epoch_iters_map[epoch] = iters
			result[epoch] = data
	return result


def generateLossCurve():
	loss_data = parseLossLogFile(LOSS_LOG_FILE)
	epochs = np.arange(1, len(loss_data), 1)
	curves = []
	labels = []
	fig = plt.figure(figsize = (14, 7))
	axes = fig.add_axes([0.05,0.07,0.9,0.9])
	for curve in ['D_A', 'D_B', 'G_A', 'G_B', 'cycle_A', 'cycle_B']:
		axes.plot(epochs, [loss_data[int(epoch)][curve] for epoch in epochs], label=TITLE_MAP[curve])
	fig.suptitle(TITLE + ' - Loss Curve', x = 0.45, y = 0.94, fontsize = 16)
	plt.legend()
	plt.show()


def fixOneLine(line):
	parts = line.split(',', 1)
	second_parts = parts[0].split(':')
	new_first_part = second_parts[0] + ': ' + str(int(second_parts[1].strip()) + 154)
	return new_first_part + ',' + parts[1]

def fixUpLog(log_file_path, new_log_file_path):
	with open(log_file_path) as loss_log:
		raw_loss_log = loss_log.readlines()
	new_raw_loss_log = []
	for line in raw_loss_log:
		new_raw_loss_log.append(fixOneLine(line))
	with open(new_log_file_path, 'w+') as new_loss_log:
		new_loss_log.writelines(new_raw_loss_log)


def main():
	generateLossCurve()
	# fixUpLog(TO_FIX, FIXED)


if __name__ == '__main__':
    main()
