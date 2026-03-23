import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kaldi running')
@cli.command()
def start(): click.echo('kaldi started')
if __name__ == '__main__': cli()
