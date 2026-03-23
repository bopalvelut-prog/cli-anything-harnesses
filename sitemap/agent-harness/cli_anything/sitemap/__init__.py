import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sitemap running')
@cli.command()
def start(): click.echo('sitemap started')
if __name__ == '__main__': cli()
