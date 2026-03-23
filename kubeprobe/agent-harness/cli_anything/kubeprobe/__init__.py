import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kubeprobe running')
@cli.command()
def start(): click.echo('kubeprobe started')
if __name__ == '__main__': cli()
