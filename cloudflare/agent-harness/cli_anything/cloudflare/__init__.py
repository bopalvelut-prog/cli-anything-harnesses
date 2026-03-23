import click
@click.group()
def cli(): pass
@cli.command()
def deploy(): click.echo('Cloudflare deploy')
@cli.command()
def workers(): click.echo('Cloudflare workers')
if __name__ == '__main__': cli()
