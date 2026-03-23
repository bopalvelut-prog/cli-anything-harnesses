import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_securitylake running')
@cli.command()
def start(): click.echo('amazon_securitylake started')
if __name__ == '__main__': cli()
