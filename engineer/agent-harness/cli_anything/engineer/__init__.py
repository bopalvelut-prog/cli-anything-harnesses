import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('engineer running')
@cli.command()
def start(): click.echo('engineer started')
if __name__ == '__main__': cli()
