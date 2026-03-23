import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apache_cloudstack running')
@cli.command()
def start(): click.echo('apache_cloudstack started')
if __name__ == '__main__': cli()
