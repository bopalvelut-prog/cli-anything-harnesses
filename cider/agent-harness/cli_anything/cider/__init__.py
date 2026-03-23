import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cider running')
@cli.command()
def start(): click.echo('cider started')
if __name__ == '__main__': cli()
