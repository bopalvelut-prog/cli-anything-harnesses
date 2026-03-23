import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloudflare_turnstile running')
@cli.command()
def start(): click.echo('cloudflare_turnstile started')
if __name__ == '__main__': cli()
