import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def score(): subprocess.run(['kube-score', 'score', 'manifest.yaml'])
if __name__ == '__main__': cli()
