import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['php', 'artisan', 'serve'])
@cli.command()
def entries(): click.echo('Statamic entries')
if __name__ == '__main__': cli()
