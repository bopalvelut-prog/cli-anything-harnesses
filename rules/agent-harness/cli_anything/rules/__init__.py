import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rules running')
@cli.command()
def start(): click.echo('rules started')
if __name__ == '__main__': cli()
