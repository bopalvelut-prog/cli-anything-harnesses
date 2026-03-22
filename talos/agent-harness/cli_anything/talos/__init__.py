import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def apply(): subprocess.run(['talosctl', 'apply-config'])
@cli.command()
def health(): subprocess.run(['talosctl', 'health'])
if __name__ == '__main__': cli()
