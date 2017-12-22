import utils
from classifiers import JobTitle
from console_logging.console import Console
console = Console()

train = utils.load_dataset('features')
console.info("Loaded training dataset.")
test = utils.load_dataset('test')
console.info("Loaded testing dataset.")
pipe = JobTitle.pipe(train)
console.success("Finished training pipe.")

t = [_['title'] for _ in test]
e = [_['categories'][0] for _ in test]

accuracy = utils.evaluate(pipe, t, e)
console.success("%f accuracy"%accuracy)

# analytics = utils.analyze(pipe, t, e, utils.categories(test))
# console.log('\n'+str(analytics))