import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Kubeflow running')
@cli.command()
def pipelines(): click.echo('Kubeflow pipelines')
if __name__ == '__main__': cli()
