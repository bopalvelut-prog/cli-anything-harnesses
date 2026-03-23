import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assembly running')
@cli.command()
def start(): click.echo('assembly started')
if __name__ == '__main__': cli()
