import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('emphasis running')
@cli.command()
def start(): click.echo('emphasis started')
if __name__ == '__main__': cli()
