import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oauth2_proxy_v2 running')
@cli.command()
def start(): click.echo('oauth2_proxy_v2 started')
if __name__ == '__main__': cli()
