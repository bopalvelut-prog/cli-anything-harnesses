import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('puppetserver running')
@cli.command()
def start(): click.echo('puppetserver started')
if __name__ == '__main__': cli()
