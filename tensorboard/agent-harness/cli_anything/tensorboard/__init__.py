import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['tensorboard', '--logdir', 'runs'])
if __name__ == '__main__': cli()
