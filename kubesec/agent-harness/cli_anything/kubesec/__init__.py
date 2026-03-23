import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kubesec running')
@cli.command()
def start(): click.echo('kubesec started')
if __name__ == '__main__': cli()
