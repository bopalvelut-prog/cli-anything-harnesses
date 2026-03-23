import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sponsor running')
@cli.command()
def start(): click.echo('sponsor started')
if __name__ == '__main__': cli()
